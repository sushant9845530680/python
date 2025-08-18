question=[
    ["Who is shah rukh khan?","WWE Wrestler","Actor","Plumber","Doctor",2],
    ["What is the capital of framce?","Paris","Romo","London","New York",1],
    ["What is the largest water animal?","Shark","Blue whale","Giraffe","Elephant",2],
]

for i in question:
 print(i[0])
 print(f"a.{i[1]}")
 print(f"b.{i[2]}")
 print(f"c.{i[3]}")
 print(f"d.{i[4]}")

 a=answer= int(input("Enter your answer:"))
 if a==i[5]:
    print("Correct answer")

else:
    print("Wrong answer")