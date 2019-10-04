import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("!! add 4 6")
        #print(response)
        self.assertEquals(response, 10)
        #self.assertEquals(response, 9)
        
        response2 = functions.get_chatbot_response("!! divide 10 5")
        #print(response)
        self.assertEquals(response2, 2)
        #self.assertEquals(response2, 4)


if __name__ == '__main__':
    unittest.main()