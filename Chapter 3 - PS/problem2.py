letter = ''' Dear < |Name| >,
            You are selected!
            <|Date|> '''

print(letter.replace("< |Name| >", "Awais").replace("<|Date|>", "1st August 2024\n"));


letter2 = ''' Dear Name,
            You are selected!
            Date '''

print(letter2.replace("Name", "Sahil").replace("Date", "1st August 2024"));


letter3 = """ Dear <Taaruf>,
            Congratulations!
            Yor are learning in 
            The Kiran Academy Pune.
            |Date| """

print(letter3.replace('<Taaruf>', 'Adnan').replace('|Date|', '9th April 2025'))