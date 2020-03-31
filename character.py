class Character:
    """Class that defines a character, characterized by:
      - its name
      - its tools"""

    def __init__(self, name):
        """Class constructor with character's name and tools inventory"""

        self.name = name
        self.tools = []

    def add_tool(self, tool):
        """Function that adds a tool in character's inventory"""

        if tool in ['N', 'T', 'E']:
            self.tools.append(tool)
