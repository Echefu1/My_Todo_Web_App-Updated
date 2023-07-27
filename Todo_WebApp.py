import streamlit as st
import functionzz

todolist = functionzz.get_todos()

def add_todo():
    todo_item = st.session_state["new_todo"]
    todolist.append(todo_item + "\n")
    functionzz.write_todos(todolist)


st.title("Echefu's Todo Web App")
st.subheader("Productivity Monitor")
st.write("Use this app to prioritize your task. ")

st.text_input(label="Add sth", placeholder="Enter your todo item:", on_change=add_todo, key='new_todo')

for index, item in enumerate(todolist):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todolist.pop(index)
        functionzz.write_todos(todolist)
        del st.session_state[item]
        st.experimental_rerun()
