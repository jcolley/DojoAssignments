
import uuid


class Call():
    def __init__(
                self,
                uid=uuid.uuid4(),
                name="",
                number="555-555-5555",
                time="00:00:00",
                reason=""
            ):
        self.uid = uid
        self.call_name = name
        self.call_number = number
        self.call_time = time
        self.call_reason = reason

    def display(self):
        for attr, value in self.__dict__.iteritems():
            print attr, value
        return self


class CallCenter():
    def __init__(self, calls):
        self.calls = calls
        self.queue = queue

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self, call):
        self.calls.remove(call[0])

    def info(self):
        for i in queue:
            print self.calls[i].call_name
            print self.calls[i].call_number
            print self.queue

call1 = Call(
        uid=uuid.uuid4(),
        name="Bob Jones",
        number="555-444-3333",
        time="12:14:55",
        reason="Help!"
    )

call2 = Call(
        uid=uuid.uuid4(),
        name="Nora Jenkins",
        number="444-111-6789",
        time="10:04:35",
        reason="Leave a message"
    )

callcenter = CallCenter().add(call1).add(call2).info()