
class Book:
    def __init__(self, title, author, state):
        self._title=title
        self._author=author
        self._state=state
    # def __str__(self):
    #     return f"Title: {self._title}, Author: {self._author}, State: {self._state}"

    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def state(self):
        return self._state

    @title.setter
    def title(self,name):
        self._title=name
    @author.setter
    def author(self,name):
        self._author=name
    @state.setter
    def state(self,state):
        self._state=state
    def print_state(self):
        print(self._title + " by "+self._author+" is "+self._state)