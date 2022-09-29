"""
File: boggle.py
Name: Yin Shih Min
----------------------------------------
User give four row of four alphabets, separate by space

"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

def main():
	"""
	User give four rows of four alphabets, separate by space, creating a 4x4 board
	The program will search all words that be formed using adjacent (up, down, left, right, and diagonal) letters
	"""
	start = time.time()
	while True:
		s1 = input('1 row of letters:')
		if len(s1) == 7 and (s1[0].isalpha() and s1[2].isalpha() and s1[4].isalpha() and s1[6].isalpha() and s1[1]==' ' and s1[3]==' ' and s1[5]==' '):
			s1 = s1.replace(' ', '').lower()
		else:
			print("Illegal input")
			break

		s2 = input('2 row of letters:')
		if len(s2) == 7 and (s2[0].isalpha() and s2[2].isalpha() and s2[4].isalpha() and s2[6].isalpha() and s2[1] == ' ' and s2[3] == ' ' and s2[5] == ' '):
			s2 = s2.replace(' ', '').lower()
		else:
			print("Illegal input")
			break


		s3 = input('3 row of letters:')
		if len(s3) == 7 and s3[0].isalpha() and s3[2].isalpha() and s3[4].isalpha() and s3[6].isalpha() and s3[1] == ' ' and s3[3] == ' ' and s3[5] == ' ':
			s3 = s3.replace(' ', '').lower()
		else:
			print("Illegal input")
			break

		s4 = input('4 row of letters:')
		if len(s4) == 7 and s4[0].isalpha() and s4[2].isalpha() and s4[4].isalpha() and s4[6].isalpha() and s4[1] == ' ' and s4[3] == ' ' and s4[5] == ' ':
			s4 = s4.replace(' ', '').lower()
		else:
			print("Illegal input")
			break

		total_str = s1+s2+s3+s4 # 把所有user key in 的字串成一個字串

		lst_word=[]
		i = 0
		for y in range(4):
			for x in range(4):
				lst = [x,y,total_str[i]] # 把每一個字串的字母，按照x,y座標包裝成[x,y,字母]
				i += 1
				lst_word.append(lst) # 包含所有[x,y,字母]的list 總和

		find_boggle(lst_word)
		break

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(lst_word):
	"""
	:param lst_word:list, contains lists that represent [x, y, letter]
	print the result of total number of words that can be found
	"""
	dictionary_list = read_dictionary()
	num_total = {}
	for num_ch in lst_word: # 從lst word中逐一開始串
		chosen_lst=[]
		chosen_lst.append(num_ch)  # 把第一個串的放在chosen_lst
		find_boggle_helper(lst_word,num_ch, num_ch[2], chosen_lst,dictionary_list, num_total)
	print('There are '+ str(len(num_total)),'word in total')

def find_boggle_helper(lst_word, start, current_s, chosen_lst,dictionary_list, num_total):
	"""
	:param lst_word: list, 包含所有[x,y,字母]的list 總和
	:param start: list, 表示從哪個字母開始找,字母為[x,y,字母]
	:param current_s:str, 目前被串起來的字
	:param chosen_lst:list, 裝已經被串過的[x,y,字母]
	:param dictionary_list:用來被搜尋的字的總和
	:param num_total: dir, 被串的總數
	"""
	# Base case
	if len(current_s) >=4:
		if current_s in dictionary_list:
			if current_s not in num_total:
				print('Found "'+current_s+'"')
				num_total[current_s] = 0

				for lst_ch in lst_word:  # 從lst_word找可以串的
					if lst_ch not in chosen_lst:  # 依序選還沒串過的
						if start[0] - 1 <= lst_ch[0] <= start[0] + 1 and 0 <= lst_ch[0] <= 3:  # 選鄰居
							if start[1] - 1 <= lst_ch[1] <= start[1] + 1 and 0 <= lst_ch[1] <= 3:
								# Choose
								current_s += lst_ch[2]  # 先串上去看看
								if has_prefix(current_s, dictionary_list):  # 找有無此開頭
									chosen_lst.append(lst_ch)  # 如果有，先放chosen_lst裡面
									find_boggle_helper(lst_word, lst_ch, current_s, chosen_lst, dictionary_list,num_total)
									chosen_lst.pop()

								current_s = current_s[:-1]



	else:
		for lst_ch in lst_word:  # 從lst_word找可以串的
			if lst_ch not in chosen_lst:  # 依序選還沒串過的
				if start[0]-1 <= lst_ch[0] <= start[0]+1 and 0<= lst_ch[0] <=3:  # 選鄰居
					if start[1] - 1 <= lst_ch[1] <= start[1] + 1 and 0<= lst_ch[1] <=3:
						# Choose
						current_s+=lst_ch[2] #先串上去看看
						if has_prefix(current_s,dictionary_list):  #找有無此開頭
							chosen_lst.append(lst_ch) # 如果有，先放chosen_lst裡面
						# Explore
							find_boggle_helper(lst_word, lst_ch, current_s, chosen_lst,dictionary_list,num_total)
						# Unchoose
							chosen_lst.pop()
						current_s = current_s[:-1]

def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_list = []
	with open(FILE, 'r') as file:
		for line in file:
			if len(line) >=4:
				dictionary_list.append(line.strip())

	# dictionary_list = set(dictionary_list)
	return dictionary_list


def has_prefix(sub_s,dictionary_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
