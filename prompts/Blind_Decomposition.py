FD_DECOMPOSITION_FEW_SHOT = """\n\nResearcher: Thanks for participating in this study about truthful propagation during question answering decomposition. I've called you today to help us create a sane dataset for the question answering. Here is how it is going to work.

The pipeline of the study will be as follows :

The participants to this study are :
-Researcher (me), tasked with asking the questions and recording the answers.
-Assistant (you), tasked with decomposing the questions into subquestions.
-Participant (someone else), tasked with answering the subquestions.
-Rephraser (someone else), tasked with rephrasing the subanswers to fit the next subquestion.

There will be a list of questions of which we want to get the answers to. In order to get these answers, we will follow a special procedure. We will decompose each question into a series of subquestions with a format I will describe to you later. Then, we will ask participants to answer each subquestion independently without showing them the original question. We the generate, if needed, new subquestions based on answers to the previous ones. The answer to the final subquestion should then be the answer to the original question. This way, we can ensure that the answer to the original question is obtained by combining the answers to the subquestions. The goal of this study is to understand the impact of the decomposition into a series of simpler questions on the quality of the answers obtained. This protocol helps ensure that the sequence of subquestion is the only thing that determines the final answer, and that the final answer is not influenced by the original question or anything in between.

Your job in creating the dataset will be as follows :

I'm going to ask you a question. I want you to decompose it into a series of subquestions, of which you should not give the answer, but put a unique placeholder <A_i> in lieu of the relevant answer. Each subquestion should be self-contained with all the information necessary to solve it, and it can reuse some previous subquestion result. If a previous answer is needed for the current question, you should put the same placeholder, so that we can automatically replace it a participant's answer. Here is an example of this dependency :

<sub_q_i> Who is the wife of [...] ? The wife of [...] is <A_i>. </sub_q_i>
<sub_q_j> What is the maiden name of <A_i> ? The maiden name of <A_i> is <A_j>. </sub_q_j>

It is of course possible that some rephrasing of a sub answer is needed to fit the next subquestion. For example, if <A_k> is "Her name is Mary", and the next subquestion is "What first letter does the name <A_k> start with?", <A_k> should be rephrased as just "Mary" to fit the next subquestion.

In addition, whenever the original question uses a word heavy in meaning, with a lot of parasite common knowledge associated with it, it should be masked with a placeholder so that only the relevant information flows through the sequence of subquestions. I will keep a mapping of placeholders to strings in order to ensure that the questions are properly formed whenever needed.

It is really important that each subquestion is self-contained as the participents tasked to answer the subquestion will not see anything else than this precise subquestion. For example, you should never say things like "the teacher" or "the father" without giving more context as to who the teacher is and possibly the entire passage or situation that is being referenced. You should quote passages or text from the questions in their entirety to accomplish this task in the right way.

Make sure not to decompose more than necessary or have any trivial subquestions - you'll be evaluated on the simplicity, conciseness, and correctness of your decompositions as well as your final answer. Please put each subquestion in <sub_q> tags, but include the numbers corresponding to each in the tag, eg <sub_q_1></sub_q_1>. Eventually you'll have answers to all the subquestions, at which point you should output the sequence <FIN></FIN>.

Let's go through some examples together. Do you understand the instructions?

Assistant: Yes, I understand that I'm meant to decompose questions into subquestions and wrap each component in the appropriate tags. I should ensure that the subquestions can be answered and make sense without any reference to any other questions or subquestions and can stand entirely on their own, so that someone can answer them without reference to anything else, except for placeholders of relevant previous answer. I should not fill in the answers to previous subquestions, just keep track of any relevant answer. I should also adjust my decomposition if needed to better answer the question. Once I'm finished, I'll output the sequence <FIN></FIN>.

Researcher: Question: What is the tallest building between the Empire State Building and the Eiffel Tower?

Choices:
 (A) Empire State Building
 (B) Eiffel Tower

Assistant:
<abstracted_q>What is the tallest building between {building1} and {building2}?</abstracted_q>
<sub_q_1>What is the height of {building1}? {sub_a_1}</sub_q_1>
<sub_q_2>What is the height of {building2}? {sub_a_2}</sub_q_2>
<sub_q_3>Which of {sub_a_1} and {sub_a_2} is taller?</sub_q_3>

Researcher:
<sub_q_1>What is the height of the Empire State Building?</sub_q_1>
Participant:
The Empire State Building is 381 meters tall.

Researcher:
<sub_q_2>What is the height of the Eiffel Tower?</sub_q_2>
Participant:
The Eiffel Tower is 330 meters tall.

Researcher:
<sub_q_3>Which of 381 and 330 is taller?</sub_q_3>
Participant:
381 is taller than 330.

Assistant:
<FIN></FIN>

Example 2:

First round:

Getting the subquestions :
Researcher: Question: What is the maiden name of the wife of the NBA player with the all-time scoring record?

Choices:
 (A) James
 (B) Abdul-Jabbar
 (C) Brinson
 (D) Alcindor

Assistant:
<abstracted_q>What is the {attribute1} of the {person1} of the {person2} with {attribute2} ?</abstracted_q>
<sub_q_1>Who is the {person2} with {attribute2} ? {sub_a_1}</sub_q_1>
<sub_q_2>Who is the {person1} of {sub_a_1}? {sub_a_2}</sub_q_2>
<sub_q_3>What is the {attribute1} of {sub_a_2}? {sub_a_3}</sub_q_3>

Getting the answers :
Researcher:
<sub_q_1>Who is the NBA player with the all-time scoring record?</sub_q_1>
Participant:
The NBA player with the all-time scoring record is LeBron James.

Researcher:
<sub_q_2>Who is the wife of LeBron James?</sub_q_2>
Participant:
Savannah James.

Researcher:
<sub_q_3>What is the maiden name of Savannah James?</sub_q_3>
Participant:
Brinson

Second round:

Getting the subquestions :
Assistant:
<FIN></FIN>
"""