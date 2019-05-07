import csv
import random
import pprint
import pandas as pd
import sys
import json


file_path = sys.argv[1]

input_file = pd.read_csv(file_path)

input_file_modified = input_file.sort_values(["Question_id","Student_score_on_question", "Quiz_score","Average_quizzes_score"], ascending = False)

# print(input_file_modified)

# input_file_modified = input_file_modified.sort_values("Question_id")

file_name = sys.argv[2]

input_file_modified.to_csv(file_name, index = None, header = True)















reader = csv.DictReader(open(sys.argv[2]))

# correct_reader = csv.DictReader()

# correct_answer_list = []

# incorrect_answer_list = []

final_correct_answer_list = []

final_incorrect_answer_list = []


question_tracker = 0.0
trigger_i = 0
answer_tracker = 1.0

j = 0

# rows = list(reader)
# totalrows = len(rows)

# new_reader = reader

for line in reader:
	# print(line)
	
	question_id = float(line["Question_id"])
	answer_value = float(line["Student_score_on_question"])

	if(question_id != question_tracker):
		question_tracker = question_id
		i = 0
		j = 0


	if(float(line["Student_score_on_question"]) < 1):
		
		# incorrect_answer_list.append(line)
		
		if(j<3):
			final_incorrect_answer_list.append(line)
			j+=1	

	else:
		# correct_answer_list.append(line)
		if(i<2):
			final_correct_answer_list.append(line)

	i+=1
	# print(i)

#Clean up unnecessary rows for ease

for item in final_incorrect_answer_list:
	del item['Average_quizzes_score'], item['Quiz_score'], item['Student_choice_on_question'], item['Student_score_on_question']



for item in final_correct_answer_list:
	del item['Average_quizzes_score'], item['Quiz_score'], item['Student_choice_on_question'], item['Student_score_on_question']


# for item in final_incorrect_answer_list:
# 	print item
# 	print ("\n")

#dict.fromkeys(['Question_id' , 'Option1'  ,'Option2' ,'Option3' ,'Option4' , 'Correct_option' ,'Feedback'])



no_of_questions = len(final_correct_answer_list)/2


final_csv_dict_array = []


# Creates as many dictionaries as needed for options
for i in range(0,len(final_correct_answer_list)/2):
	final_csv_dict_array.append(dict.fromkeys(['Question_id' ,'Question', 'Option1'  ,'Option2' ,'Option3' ,'Option4' , 'Correct_option' ,'Feedback']))




i = 0
j = -3
for item in final_correct_answer_list:
	# print(i)
	if i%2 == 0:
		correct_option_indice = random.randint(1,4)
		# correct_option_id = "Option1"


		if correct_option_indice == 1:
			correct_option_id = "Option1"
		if correct_option_indice == 2:
			correct_option_id = "Option2"
		if correct_option_indice == 3:
			correct_option_id = "Option3"
		if correct_option_indice == 4:
			correct_option_id = "Option4"


		
		final_csv_dict_array[i/2]["Question_id"] = item["Question_id"]
		final_csv_dict_array[i/2]["Feedback"] = item["Answer_text"]
		final_csv_dict_array[i/2]["Correct_option"] = correct_option_id
	else:
		final_csv_dict_array[(i-1)/2][correct_option_id] = item["Answer_text"]				
	i+=1

i = 0
j = 0


for j in range(0,no_of_questions*3):
	if(j%3 == 0):
		if final_csv_dict_array[j//3]["Option1"] is None:
			final_csv_dict_array[j//3]["Option1"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option2"] is None:
			final_csv_dict_array[j//3]["Option2"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option3"] is None:
			final_csv_dict_array[j//3]["Option3"] = final_incorrect_answer_list[j]["Answer_text"]
		else:
			final_csv_dict_array[j//3]["Option4"] = final_incorrect_answer_list[j]["Answer_text"]

	if(j%3 == 1):
		if final_csv_dict_array[j//3]["Option1"] is None:
			final_csv_dict_array[j//3]["Option1"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option2"] is None:
			final_csv_dict_array[j//3]["Option2"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option3"] is None:
			final_csv_dict_array[j//3]["Option3"] = final_incorrect_answer_list[j]["Answer_text"]
		else:
			final_csv_dict_array[j//3]["Option4"] = final_incorrect_answer_list[j]["Answer_text"]
		
	if(j%3 == 2):
		if final_csv_dict_array[j//3]["Option1"] is None:
			final_csv_dict_array[j//3]["Option1"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option2"] is None:
			final_csv_dict_array[j//3]["Option2"] = final_incorrect_answer_list[j]["Answer_text"]
		elif final_csv_dict_array[j//3]["Option3"] is None:
			final_csv_dict_array[j//3]["Option3"] = final_incorrect_answer_list[j]["Answer_text"]
		else:
			final_csv_dict_array[j//3]["Option4"] = final_incorrect_answer_list[j]["Answer_text"]


final_csv_dict_array = final_csv_dict_array[::-1]


question_reader = csv.DictReader(open(sys.argv[3]))

for line in question_reader:

	question = line["Question_text"]
	question_id = int(line["Question_id"])

	for item in final_csv_dict_array:
		if int(item["Question_id"]) == question_id:
			item["Question"] = question 




# for item in final_csv_dict_array:
# 	print item
# 	print ("\n")


# keys = ['Question_id' , 'Question' ,'Option1'  ,'Option2' ,'Option3' ,'Option4' , 'Correct_option' ,'Feedback']
# with open(sys.argv[4], 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(final_csv_dict_array)


json_quiz_array = []

for element in final_csv_dict_array:
	data_object = {}
	data_object["question"] = element["Question"]
	data_object["choices"] = [element["Option1"], element["Option2"], element["Option3"], element["Option4"]]
	data_object["correct"] = [element[element["Correct_option"]]] 
	data_object["explanation"] = element["Feedback"]

	json_quiz_array.append(data_object)

with open("jsonText1.json",'w') as fp:
	json.dump(json_quiz_array,fp)


second_json_quiz_array = []




# for item in final_csv_dict_array: 
# 	item["Option 1"] = item.pop("Option1")
# 	item["Option 2"] = item.pop("Option2")
# 	item["Option 3"] = item.pop("Option3")
# 	item["Option 4"] = item.pop("Option4")
# 	item["Correct Answer"] = item.pop("Correct_option")
	
# 	del item["Feedback"]
# 	del item["Question_id"]


# for item in final_csv_dict_array:
# 	print item
# 	print ("\n")


# quizzit_keys = ['Question' ,'Option 1'  ,'Option 2' ,'Option 3' ,'Option 4', 'Correct Answer']
# with open(sys.argv[5], 'wb') as output_file:
#     new_dict_writer = csv.DictWriter(output_file, quizzit_keys)
#     new_dict_writer.writeheader()
#     new_dict_writer.writerows(final_csv_dict_array)



# print(len(final_correct_answer_list))



