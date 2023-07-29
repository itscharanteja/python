class ReverseString:
    def get_input(self):
        # get input string from user
        s = input("Enter a string: ")
        return s

    def reverse_word_by_word(self, s):
        # split the string into words
        # words = s.split()
        # reverse the words
        reverse = s[::-1]
        # join the words back together
        reversed_string = ' '.join(reverse)
        return reversed_string


r = ReverseString()
s = r.get_input()
reversed_string = r.reverse_word_by_word(s)
print(reversed_string)
