from random import randint


def pick_ques_list(all_ques_list,user_ques_perc):
      std_ques_list=[]
      ques_ind_list=[]      
      all_ques_count = len(all_ques_list)
      ques_count = round(all_ques_count * user_ques_perc)

      for i in range(ques_count):
            index = randint(0,all_ques_count-1)
            while index in ques_ind_list:
                  index = randint(0,all_ques_count-1)                  
            std_ques_list.append(all_ques_list[index])
            ques_ind_list.append(index)
      return([std_ques_list,ques_ind_list])


def show_ques_read_answers(std_ques_list):
      std_ans_list =[]
      for i in range(len(std_ques_list)):
            ans = input(f"--> {i+1}) {std_ques_list[i]} : ")
            std_ans_list.append(ans)
      return(std_ans_list)


def sum_true_ans(std_ans_list,ques_ind_list,all_true_ans_list):
      total_true_ans = 0
      all_ans_count =len(std_ans_list) 
      for i in range(all_ans_count):
            if std_ans_list[i].lower() == all_true_ans_list[ques_ind_list[i]].lower():
                  total_true_ans += 1           
      return (total_true_ans)


def check_total (total_degree,total_all,total_min_perc):
      return(total_degree >= total_min_perc * total_all)


def main():
      
      all_ques_list = [
            "What is the capital of Algeria?",
            "What is the capital of Bahrain?",
            "What is the capital of Comoros?",
            "What is the capital of Djibouti?",
            "What is the capital of Egypt?",
            "What is the capital of Iraq?",
            "What is the capital of Jordan?",
            "What is the capital of Kuwait?",
            "What is the capital of Lebanon?",
            "What is the capital of Libya?",
            "What is the capital of Mauritania?",
            "What is the capital of Morocco?",
            "What is the capital of Oman?",
            "What is the capital of Palestine?",
            "What is the capital of Qatar?",
            "What is the capital of Saudi Arabia?",
            "What is the capital of Somalia?",
            "What is the capital of Sudan?",
            "What is the capital of Syria?",
            "What is the capital of Tunisia?",
            "What is the capital of United Arab Emirates?",
            "What is the capital of Yemen?" ]

      all_true_ans_list = [
            "Algiers",
            "Manama",
            "Moroni",
            "Djibouti",
            "Cairo",
            "Baghdad",
            "Amman",
            "Kuwait City",
            "Beirut",
            "Tripoli",
            "Nouakchott",
            "Rabat",
            "Muscat",
            "Jerusalem",
            "Doha",
            "Riyadh",
            "Mogadishu",
            "Khartoum",
            "Damascus",
            "Tunis",
            "Abu Dhabi",
            "Sana'a" ]

      user_ques_perc = 0.25 # نسبة اختيار الأسئلة
      total_min_perc = 0.50 # نسبة النجاح الدنيا لإجمالي الإختيار

      [std_ques_list,ques_ind_list] = pick_ques_list(all_ques_list,user_ques_perc)

      std_ans_list = show_ques_read_answers(std_ques_list)

      total_degree = sum_true_ans(std_ans_list,ques_ind_list,all_true_ans_list)
      
      total_all = len(std_ques_list)
      qualified = check_total(total_degree,total_all,total_min_perc)
      if (qualified):
            print(f'Great {total_degree} true answers. You are READY for learning')      
      else: 
            print(f'Sorry only {total_degree} true answers. You are NOT READY for learning')


if __name__=='__main__':
      main()