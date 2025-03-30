import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image )
     
df = pd.read_csv("50_states.csv ")

with open("score_data", mode= "w") as file:
    file.write("0")



guessed_states = []
score = 0
state_list = df["state"].to_list()
while len(guessed_states) < 50:
   answer_state = screen.textinput(title=f"state{score}/{50} ", prompt= "What's another state's name").title() 


   #check if state is among the 50 states of us

   if  answer_state == "Exit":
         missing_states = [state for state in state_list if state not in guessed_states]

         new_data = pd.DataFrame(missing_states )
         new_data.to_csv("States_to_learn.csv")
         break


   if answer_state.title()   in  state_list:
      score +=1
      guessed_states.append(answer_state )
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      row = df[df.state == answer_state]
      x = row.x
      y = row.y
      t.goto(int(x),int(y))
      t.write(answer_state  )




