import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    todo=todo + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")
st.write("Your bed time starts after deciding tomorrow's todo list.")

for index,todo in enumerate(todos):
    checked=st.checkbox(todo, key=index)
    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="Enter Todo ",placeholder="Add new todo....",
    on_change=add_todo,key="new_todo")

#print ("hello")
st.session_state