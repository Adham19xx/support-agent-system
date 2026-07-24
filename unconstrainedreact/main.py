from agent import run_agent


user_message = input("Enter your problem: ")


response = run_agent(user_message)


print(response)
