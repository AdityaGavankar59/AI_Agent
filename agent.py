from intents import detect_intent
from features.weather import get_weather
from features.calculator import calculate
from features.wiki import wiki_summary
from features.todo import TodoList
from features.jokes import tell_joke

class Agent:
    def __init__(self):
        self.todos = TodoList()
        self.running = True

    def handle_intent(self, intent, slots):
        if intent == "exit":
            self.running = False
            return "Goodbye! 👋"

        if intent == "help":
            return (
                "I can do:\n"
                "- weather <city>\n"
                "- calc <expression>\n"
                "- wiki <topic>\n"
                "- add todo <task>\n"
                "- list todos\n"
                "- joke\n"
                "- exit\n"
            )

        if intent == "weather":
            city = slots.get("city")
            if not city:
                return "Please tell me a city, e.g., 'weather Mumbai'."
            return get_weather(city)

        if intent == "calc":
            expr = slots.get("expr")
            if not expr:
                return "Please give me an expression, e.g., 'calc 2+3*4'."
            return calculate(expr)

        if intent == "wiki":
            topic = slots.get("topic")
            if not topic:
                return "Please provide a topic, e.g., 'wiki machine learning'."
            return wiki_summary(topic)

        if intent == "add_todo":
            task = slots.get("task")
            if not task:
                return "What should I add to your to-do list?"
            self.todos.add(task)
            return f"Added to your to-do list: {task}"

        if intent == "list_todo":
            return self.todos.list_items()

        if intent == "joke":
            return tell_joke()

        return "Sorry, I didn't understand that. Type 'help' to see what I can do."

def main():
    agent = Agent()
    print("AI Agent ready. Type 'help' to see commands, 'exit' to quit.")

    while agent.running:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Goodbye!")
            break

        if not user_input:
            continue

        intent, slots = detect_intent(user_input)
        response = agent.handle_intent(intent, slots)
        print(response)

if __name__ == "__main__":
    main()
