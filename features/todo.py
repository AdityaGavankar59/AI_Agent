class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task: str):
        self.items.append(task.strip())

    def list_items(self) -> str:
        if not self.items:
            return "Your to-do list is empty."
        lines = [f"{i+1}. {item}" for i, item in enumerate(self.items)]
        return "Your to-do list:\n" + "\n".join(lines)
