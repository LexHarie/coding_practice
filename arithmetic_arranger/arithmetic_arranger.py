def arithmetic_arranger(problems, reveal = False):
  my_list = []
  my2_list = []
  
  
  for problem in problems:
      my_list = problem.split()
      my2_list.extend(my_list)
  
  
  first_numbers = my2_list[0::3]
  operations = my2_list[1::3]
  second_numbers = my2_list[2::3]
  fake_total = []
  real_total = []
  operation_plus_second_number = []
  dashes = []
  white_spaces = []
  white_space = None
  
  for i in range(len(problems)):  
      if operations[i] == '+':
          fake_total.append(int(first_numbers[i]) + int(second_numbers[i]))
      elif operations[i] == '-':
          fake_total.append(int(first_numbers[i]) - int(second_numbers[i]))
  
  
  number_of_dashes = None
  for i in range(len(problems)):
      number_of_dashes = max(len(first_numbers[i]),len(second_numbers[i]))+ 2
      dashes.append(number_of_dashes*'-')
  #print(dashes)
  
  
  
  for item in range(len(problems)):
      white_space = len(dashes[item]) - len(operations[item]) -len(second_numbers[item])
      operation_plus_second_number.append(operations[item] + ' '*white_space + second_numbers[item])
      
  
      
  
  #the white space is equal to len(dashes) - len(first_number)
  #then we add the white space to the str(first_number) then we add four white spaces
  
  
  for i in range(len(problems)):
      white_space = len(dashes[i]) - len(first_numbers[i])
      white_spaces.append(" "*white_space)
      
  #We need white-spaces for the total, and to do that, we have to get the difference len(dashes) minus the len(total)
  #the number of white space is the difference.
  
  for i in range(len(problems)):
      white_space = len(dashes[i]) - len(str(fake_total[i]))
      real_total.append(" "*white_space + str(fake_total[i]))
  
  first_order = []
  word = ''
  for i in range(len(problems)):
      first_order.append(white_spaces[i]+first_numbers[i]+'    ')
      
      
  second_order = []
  for i in range(len(problems)):
      second_order.append(operation_plus_second_number[i] + '    ')
      
  third_order = []
  for i in range(len(problems)):
      third_order.append(dashes[i] + '    ')
  
  fourth_order = []
  for i in range(len(problems)):
      fourth_order.append(str(real_total[i]) + '    ')
  
  
  first_line = ''.join(first_order)
  second_line = ''.join(second_order)
  third_line = ''.join(third_order)

  if reveal:
    fourth_line = ''.join(fourth_order)
    return f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}"
  else:
    return f"{first_line}\n{second_line}\n{third_line}"