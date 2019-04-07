# -*- coding: utf-8 -*-
import re
from chatterbot.logic import LogicAdapter
import urllib.parse
import urllib.request
import json

class MedDatabaseAdapter(LogicAdapter):
    """
    A logic adapter that returns information regarding medicine information
    """

    def process(self, statement):
        """
        Returns the info.
        """
        from chatterbot.conversation import Statement

        user_input = statement.text.lower()

        if ('medicine' and 'manufacturer') not in user_input:
            
            response_statement = Statement('')
            response_statement.confidence = 0
            return response_statement


        medicine = self.get_med(user_input)

        if medicine is not '':
            response_statement = Statement(self.get_info(medicine))
            response_statement.confidence = 1
            return response_statement

        response_statement = Statement('')
        response_statement.confidence = 0
        return response_statement

    def get_med(self, user_input):
        """
        Returns the medicine name extracted from input.
        """
        from nltk import tokenize

        for token in tokenize.word_tokenize(user_input):
            if 'medicine' in token:
                #return (re.sub('medicine', '', user_input).lstrip())
                return (user_input.split('medicine')[1]).lstrip()

        return ''
    def get_info(self, medicine):
        """
        Returns the info from webserver.
        """

        # @TODO: Find some way to suppress the warnings generated by this.
        Data=[('brandname',medicine)]
        Data=urllib.parse.urlencode(Data).encode("utf-8")
        path="http://fs1.jayapraveenar.me/RIBA/meddb.php"
        request=urllib.request.Request(path,Data)
        request.add_header("Content-type","application/x-www-form-urlencoded")
        output=urllib.request.urlopen(request).read()
        #print output
        out= json.loads(output)
        #print (out['Manufacturer'])
        return (out['Manufacturer'])