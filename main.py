chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

def get_char_count_dictionary(chars,book):
	book = book.lower()
	my_dictionary={}
	for char in chars:
		my_dictionary[char]=book.count(char)
	return my_dictionary

def get_book_text():
	with open("/home/ali_zaman_1/workspace/github.com/musab-ibn-ali/bookbot/books/frankenstein.txt") as f:
		file_contents=f.read()
	return file_contents

def count_words(my_book_text):
	return len(my_book_text.split())

def sort_on(dicti):
	return dicti["count"]

def convert_to_sorted_dicti_list(char_count_dictionary):
	dicti_list=[{key:value,"count":value} for key,value in char_count_dictionary.items()]
	dicti_list.sort(reverse=True,key=sort_on)
	for dicti in dicti_list:
		dicti.pop("count")
	return dicti_list

def create_book_report():
	print("--- Begin report of books/frankstein.txt ---")
	book=get_book_text()
	word_count=count_words(book)
	print(f"{word_count} words found in the document")
	print('')
	print('')
	my_char_count_dictionary=get_char_count_dictionary(chars,book)
	my_char_count_dictionary_list=convert_to_sorted_dicti_list(my_char_count_dictionary)
	for dicti in my_char_count_dictionary_list:
		kv=[[key,value] for key,value in dicti.items()]
		print(f"The '{kv[0][0]}' character was found {kv[0][1]} times")

def main():
	#print(get_book_text())
	create_book_report()


main()
