from Participant import Participant
from STUDYGROUP import STUDYGROUP
from Task import Task, RESULTTYPE
from display_DOU import display_DOU
from display_TTU import display_TTU

p01 = Participant(id="p01", studygroup=STUDYGROUP.F)
p31 = Participant(id="p31", studygroup=STUDYGROUP.F)
p34 = Participant(id="p34", studygroup=STUDYGROUP.F)
p33 = Participant(id="p33", studygroup=STUDYGROUP.F)
p26 = Participant(id="p26", studygroup=STUDYGROUP.F)
p21 = Participant(id="p21", studygroup=STUDYGROUP.F)
p27 = Participant(id="p27", studygroup=STUDYGROUP.F)

p11 = Participant(id="p11", studygroup=STUDYGROUP.S)
p30 = Participant(id="p30", studygroup=STUDYGROUP.S)
p28 = Participant(id="p28", studygroup=STUDYGROUP.S)
p09 = Participant(id="p09", studygroup=STUDYGROUP.S)
p14 = Participant(id="p14", studygroup=STUDYGROUP.S)
p15 = Participant(id="p15", studygroup=STUDYGROUP.S)
p02 = Participant(id="p02", studygroup=STUDYGROUP.S)

p03 = Participant(id="p03", studygroup=STUDYGROUP.V)
p05 = Participant(id="p05", studygroup=STUDYGROUP.V)
p04 = Participant(id="p04", studygroup=STUDYGROUP.V)
p20 = Participant(id="p20", studygroup=STUDYGROUP.V)
p07 = Participant(id="p07", studygroup=STUDYGROUP.V)
p38 = Participant(id="p38", studygroup=STUDYGROUP.V)
p06 = Participant(id="p06", studygroup=STUDYGROUP.V)


participants = [p01, p31, p34, p33, p26, p21, p27,
                p11, p30, p28, p09, p14, p15, p02,
                p03, p05, p04, p20, p07, p38, p06]



t1 = Task(1, description="Calculate the Total Price for Apples by multiplying their Quantity and Item Price.", formula="",
          expected_result_cell="F4", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t2 = Task(2, description="Calculate the Net Subtotal by adding the Total Prices of all invoiced items.", formula="",
          expected_result_cell="F14", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=4)
t3 = Task(3, description="Calculate the Gross Subtotal by adding 15% tax to the Net Subtotal.", formula="",
          expected_result_cell="F15", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t4 = Task(4, description="Calculate the Quantity of Orange Juice.", formula="",
          expected_result_cell="A9", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t5 = Task(5, description="Identify the maximum of all Discounts, and display it in cell J4.", formula="",
          expected_result_cell="J4", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=4)
t6 = Task(6, description="Calculate the average of all Item Prices, round the result to the nearest whole task_number, and display it in cell J5.", formula="",
          expected_result_cell="J5", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t7 = Task(7, description="Calculate the Packaging Fee by multiplying the Delivery Fee with the maximum of all Quantities and the average of all Discounts, and rounding the result to the nearest whole task_number.", formula="",
          expected_result_cell="F16", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=9)
t8 = Task(8, description="Assuming there is a 'get one free' deal for Chocolate, calculate its Total Price.", formula="",
          expected_result_cell="F10", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=7)
t9 = Task(9, description="Calculate the Total Price for each individual item by multiplying its Quantity and Item Price and applying the Discount.", formula="",
          expected_result_cell="F4:F12", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.LIST, max_total=7)
t10 = Task(10, description="Set the Delivery Fee to 10 € if the Gross Subtotal is less than 100 €, or 20 € otherwise.", formula="",
          expected_result_cell="F17", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=8)
t11 = Task(11, description="Calculate the Invoice Amount by subtracting the Customer Credit from the Grand Total.", formula="",
          expected_result_cell="F26", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t12 = Task(12, description="Calculate the Express Fee (in the Invoice) by multiplying the Gross Subtotal with the Express Rate (in the Inventory).", formula="",
          expected_result_cell="F18", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t13 = Task(13, description="Calculate the Invoice Amount by subtracting the Customer Credit and the Holiday Discount (in the Inventory) from the Grand Total.", formula="",
          expected_result_cell="F26", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=6)
t14 = Task(14, description="Determine the Item Price of Wine (in the Invoice) by using its Item No. to look up its Unit Price in the Inventory?", formula="",
          expected_result_cell="D6", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=5)
t15 = Task(15, description="Calculate the Item Price of Laundry Detergent (in the Invoice) by adding the Low Stock Surcharge (in the Inventory) to its Unit Price if its Stock is lower than 5.", formula="",
          expected_result_cell="D12", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.VALUE, max_total=11)
t16 = Task(16, description="List the Item No's of all items whose Stock is lower than 5 next to'Low stock' in the Inventory?", formula="",
          expected_result_cell="Inventory formulars'C7:G7", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.LIST, max_total=8)
t17 = Task(17, description="List the Item No's of all invoiced items that are not included in the Inventory under 'Unknown items' in the Invoice.", formula="",
          expected_result_cell="H9:H10", expected_operations = "", expected_operands="",
          result_type=RESULTTYPE.LIST, max_total=7)

tasks = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17]



for p in participants:
    for t in tasks:
        p.create_task_files(task=t)



display_DOU(participants=participants, task_ids=[i for i in range(1,18)])
display_TTU(participants=participants, task_ids=[i for i in range(1,18)])