def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text
    # turn a doc into clean tokens
    
def get_sender(begin,note):
    x=note[0:begin]
    first_sender=note[2:4]
    if first_sender=='dr':
        second_sender='Pt'
    else:
        second_sender='Dr' 
        first_sender="Pt"
    newlines = len(x.split('\n'))
    if newlines%2==1:
        return first_sender
    else:
        return second_sender
    
file_no=4030
note=load_doc("E:/HZ/my_papers/your doctor online/chats_unified_consecutive_msgs_gropued_1-1000/"+str(file_no)+".txt")
note_without_newline=note.replace('\n', '__')
import pandas as pd

import webbrowser
filename="E:/HZ/my_papers/your doctor online/quiz/test/Q"+str(file_no)+".html"
f = open(filename,'w')

message_tbl = """<html>
<head>
<script type="text/javascript">

var row_no="0";
var answer='x';
  function OnRowClick (row) {
			q_no="q"+row.rowIndex;
			if(answer!='x') // if no option is made
			  {
				answer_int=parseInt(answer);
				var colors = ['#ffeeee', '#ddffdd', '#88ff77','#00ee00'];
				document.getElementById(q_no).style.backgroundColor = colors[answer_int];
				answer='x';
			}
        }



function f(t)
{
answer=t.value;
}
//////////////////////////////////////
function collect(){
var all_ans="";
var tot_questions = document.getElementById("questionnaire").rows.length;


var un_answered_no=0
var The_answered=-1;

for (var qn = 1; qn < tot_questions; qn++)
{
var question = document.getElementsByName("a"+qn);
The_answered=-1;
for(var i = 0; i < question.length; i++) 
{
   if(question[i].checked)
   {
       importance = question[i].value;
       all_ans=all_ans+qn+':'+importance+', ';
	   The_answered=i;  
}
}
if (The_answered==-1){
 un_answered_no++;
  //alert(qn);
 }



}
if (un_answered_no>0)
 alert('please anwer all questions ('+un_answered_no+' are null now)'); 
 else
 {
result.value="document number:"+doc_no.value+", Doctor's name: "+Dr_name.value+"|"+all_ans;
copy_msg.style.visibility = 'visible';
}
}

</script>
</head>



<body bgcolor="#eeffff">

Please enter your name: <input type="text" size="10" id="Dr_name" >
<Br>

<Br>
Doc No: <input type="text" value="""+str(file_no)+""" size="10" id="doc_no" disabled>
<br>
<br>

<table border="1" cellspacing="0" cellpadding="5" id="questionnaire" bgcolor="#ffffff">
<thead>
<th>Message#</th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>Message</th>
</thead>
<tbody>

"""
 

#====================================================================================

import pysbd
seg = pysbd.Segmenter(language="en", clean=False)
idx=0
loc=0
for sentence in seg.segment(note):
    idx+=1
    sender=get_sender(loc+1,note)
    loc+=len(sentence)
    message_tbl=message_tbl+"""
    <tr  onclick='OnRowClick (this)' id='row"""+str(idx)+"""'>
    <td>"""+str(idx)+"""</td>

    <td border="0"><input type='radio' name='a"""+str(idx)+"""' value='0'  onclick='f(this)'></td>
    <td border="0"><input type='radio' name='a"""+str(idx)+"""' value='1' onclick='f(this)'></td>
    <td border="0"><input type='radio' name='a"""+str(idx)+"""' value='2' onclick='f(this)'></td>
   <td border="0"> <input type='radio' name='a"""+str(idx)+"""' value='3' onclick='f(this)'></td>
    </td>
    <td id='q"""+str(idx)+"""'>"""+sender+": "+ sentence+""" </td> </tr>"""


message_tbl=message_tbl+"""</table><br>

	<input type="button" value="Collect the answers" onclick="collect()" style="font-size: 14pt; background-color: #4CAF50;">
	<br>
	<br>
	<div id='copy_msg' style="visibility:hidden">
	<p style="font-size: 14pt; color: #FF1122;"> Please copy the content of the following textbox and send it to the following email: </P>
	<p style="font-size: 14pt; color: #1111ff;"> zafari@cs.queensu.ca </p> 
	<p> Thanks </p>
	</div>

    <br>
	<br>
	<textarea id="result" name="w3review" rows="4" cols="150" style="font-size: 14pt"></textarea>
	
		
	</body></html>


"""




f.write(message_tbl)
f.close()

webbrowser.open_new_tab(filename)