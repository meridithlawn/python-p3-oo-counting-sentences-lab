#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = value
    
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    value = self.value
    for punctuation in ["!", "?"]:
      value = value.replace(punctuation, ".")
    num_sentences = [sentence for sentence in value.split(".") if sentence]
    return len(num_sentences)
    
    # for each sentence in value, loop through to split at "." and then
    # if it is a sentence, it will return true and be added to the array 
    # which we indicated with the brackets

    # be careful with indentation with for loops etc


