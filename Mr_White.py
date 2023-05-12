import discord
from discord.ext import commands
import random
import asyncio
import os




client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


bedtime_stories =[
    "The Lion and the Mouse: Once upon a time, a little mouse accidentally woke up a lion while playing. The lion was angry and was about to eat the mouse when the mouse begged for forgiveness and promised to repay the lion's kindness someday. The lion laughed and let the mouse go. Later on, the lion got caught in a hunter's trap, and the mouse came to his rescue by nibbling away at the ropes. From that day on, the lion and the mouse became the best of friends.",
    "The Ugly Duckling: In a farmyard, a mother duck hatched a clutch of eggs, but one of the ducklings was much bigger and clumsier than the others. The other animals teased him and made him feel unwanted. He ran away to find somewhere he belonged, and after many adventures, he discovered he was actually a swan. He joined a family of swans and was finally happy and loved for who he truly was.",
    "The Three Little Pigs: Three little pigs left their mother's home to build their own houses. The first pig built a house of straw, the second pig built a house of sticks, and the third pig built a house of bricks. A big bad wolf came to the first two pigs' houses and blew them down, but the third pig's brick house was too strong. The wolf tried to climb down the chimney, but the clever pig put a pot of boiling water on the fire, and the wolf fell in and ran away. The three little pigs lived happily ever after in their safe and sturdy home.",
    "The Tortoise and the Hare: In a forest, a hare boasted about his speed to a tortoise, who challenged him to a race. The hare took off at lightning speed but stopped to rest, thinking he had plenty of time to win. The tortoise continued at a slow but steady pace, and when the hare woke up, the tortoise was almost at the finish line. The hare tried to catch up, but it was too late, and the tortoise won the race. The moral of the story is slow and steady wins the race.",
    "The Little Mermaid: In the depths of the ocean, a mermaid fell in love with a human prince and made a deal with a sea witch to become human in exchange for her voice. She went to live on land but had to win the prince's love before sunset on the third day, or she would turn back into a mermaid and belong to the sea witch. She faced many obstacles but finally won the prince's love with her kindness and courage. They lived happily ever after on land, and the mermaid's father allowed her to stay human because he saw how much she had grown and matured.",
    "The Boy Who Cried Wolf Once upon a time, there was a boy who lived in a village. He would often play tricks on the villagers by shouting Wolf! Wolf! when there was no wolf. One day, a wolf actually came, and the boy cried out for help, but nobody believed him. From that day on, the boy learned the importance of telling the truth.",
    "The Little Red Hen: Once upon a time, there was a little red hen who lived on a farm. She wanted to make some bread, but none of the other animals on the farm would help her. So she did all the work herself and enjoyed the bread all by herself. The moral of the story is, If you want to enjoy the fruits of someone else's labor, you must first be willing to help.",
    "The Tortoise and the Hare: A hare was boasting about how fast he could run, and a tortoise challenged him to a race. The hare thought it was a joke, but the tortoise was serious. During the race, the hare got tired and decided to take a nap, but the tortoise kept going and won the race. The moral of the story is, Slow and steady wins the race.",
    "The Lion and the Mouse: A lion was caught in a hunter's trap, and a little mouse came along and freed him. Later, the lion returned the favor by saving the mouse from a cat. The moral of the story is,Even the smallest acts of kindness can be repaid in unexpected ways.",
    "The Little Mouse and the Big Hungry Bear: Once upon a time, there was a little mouse who lived in a tiny house in the forest. One day, the mouse found out that there was a big hungry bear lurking around, looking for a tasty meal. The mouse was afraid, but he came up with a clever plan to outsmart the bear. He told the bear that he had a delicious cake hidden in his house, but he needed some ingredients to make it. The bear fell for the trick and went to get the ingredients, but while he was gone, the mouse escaped.",
    "Little Red Riding Hood: Little Red Riding Hood was on her way to visit her grandmother when she met a wolf. The wolf tricked her into telling him where her grandmother lived and then ate her. Little Red Riding Hood learned that it's important to be careful around strangers.",
    "The Boy Who Cried Wolf:A boy who watched over sheep pretended that a wolf was attacking them. When the villagers came to his rescue, they realized he was lying. The boy did this several times, and when a real wolf finally came, nobody believed him, and the wolf ate the sheep. The boy learned that it's important to tell the truth.",
    "The Emperor's New Clothes:An emperor loved new clothes and hired two weavers to make him an outfit made of fabric that was invisible to anyone who was unfit for their position or stupid. The weavers pretended to weave the fabric, and the emperor pretended to wear the outfit. When he paraded in front of his subjects, a child pointed out that the emperor was wearing no clothes at all. The emperor learned that appearances can be deceiving.",
    "The Fisherman and His Wife:A fisherman caught a magic fish that promised to grant him wishes. He wished for a bigger house, and his wife wished for more and more until she wished to be queen. The fish granted all their wishes, but the wife was never satisfied. In the end, the fish took away all their wealth, and they were back where they started. They learned to be grateful for what they had.",
    "The Gingerbread Man:A woman baked a gingerbread man who ran away from her. As he ran, he met several animals who wanted to eat him. He was too fast for them until he met a sly fox who tricked him into getting too close. The fox ate the gingerbread man, who learned that it's not always safe to trust strangers.",
    "The Elephant and the Ant: An elephant accidentally stepped on an ant's nest and apologized. The ant forgave him and offered to help him in the future. The elephant didn't believe that the tiny ant could be of any use, but when he got stuck in mud, the ant helped him out. The elephant learned that size doesn't matter.",
    "The Unicorn's Gift:A young girl loved unicorns and wished she could have one. One day, a unicorn appeared to her and granted her wish, but she soon realized that taking care of a unicorn was a big responsibility. She decided to return the unicorn to the forest, and the unicorn gave her a special gift to remember their time together.",
    "The Dragon and the Princess: A dragon lived in a castle and demanded that the nearby kingdom provide him with a princess to marry. The princess he chose, however, was not content with being a dragon's wife and devised a plan to escape. With the help of a brave knight, she defeated the dragon and married the knight instead.",
    "The Magic Garden:A little boy discovered a magic garden that only he could see. In the garden, he met talking animals and plants that taught him important lessons about life. When he left the garden, he realized that he could carry the magic with him wherever he went.The Mermaid's Secret:",
    "The Mermaid's Secret: A young girl loved the ocean and dreamed of meeting a mermaid. One day, a mermaid appeared to her and invited her to explore the underwater world. The girl learned that the ocean was in danger, and the mermaid revealed a secret that only she could help with.",
    "The Enchanted Forest:A brother and sister were lost in an enchanted forest, where they met fairies and other magical creatures. They were frightened at first, but as they learned more about the forest, they realized that it held many secrets and wonders that they could explore forever.",
    "The Wizard's Apprentice:A young boy dreamed of becoming a wizard and was taken on as an apprentice by an old wizard. The boy learned magic and went on many adventures with the wizard until he was ready to become a wizard himself.",
    "The Fairy Princess:A young girl discovered a fairy kingdom in her garden and became friends with the fairy princess. The princess taught her about the magical world of fairies and their customs. The girl helped the princess in a time of need, and the two became lifelong friends.",
    "The Giant and the Beanstalk:A boy discovered a magic bean and planted it in his garden. The bean grew into a giant beanstalk that reached the clouds. The boy climbed the beanstalk and met a giant who lived in the sky. The giant taught him valuable lessons about life and helped him find his way back home.",
    "The Talking Animal Kingdom:A young girl stumbled upon a kingdom of talking animals, where she was greeted by the wise old owl who taught her about the importance of kindness and friendship. She made many friends in the animal kingdom and learned that everyone is unique and special in their own way.",
    "The Flying Carpet:A brother and sister discovered a flying carpet in their attic and took it on an adventure across the world. They visited many different cultures and learned about the people and places they encountered. The flying carpet taught them that the world is full of wonder and beauty",
    "The Magic Mirror:A young girl received a magic mirror as a gift from her fairy godmother. The mirror revealed her true self, but she became obsessed with her reflection and forgot about the people and things that mattered most. With the help of her friends, she learned that beauty is not just skin deep.",
    "The Sorcerer's Stone:A young boy discovered a sorcerer's stone that gave him the power to bring inanimate objects to life. He used his power to create a world of wonder and imagination, but soon realized that his power had consequences. With the help of his friends, he learned that with great power comes great responsibility.",
    "The Dragon's Treasure:A group of adventurers set out to find a dragon's treasure, but instead of riches, they found a dragon who was lonely and wanted friends. They befriended the dragon, and together, they went on many adventures and discovered that friendship is the greatest treasure of all.",
    "The Enchanted Toy Shop:A young girl wandered into an enchanted toy shop where the toys came to life. She played with them all day and learned that sometimes the best adventures are found in the simplest of places.",
    "The Secret Garden:A young girl discovered a secret garden that was overgrown with weeds. She worked hard to restore it to its former glory and discovered that the garden was magical. With the help of her friends, she learned that sometimes the things that seem broken and forgotten can be the most beautiful.",
    "The Magic Lamp:A young boy discovered a magic lamp with a genie inside who granted him three wishes. The boy used his wishes wisely and learned that sometimes the greatest happiness comes from the simplest things in life.",
    "The Enchanted Castle:A young princess was trapped in an enchanted castle by an evil sorcerer. With the help of a brave knight, she escaped and defeated the sorcerer, but learned that sometimes the greatest strength comes from within.",
    "The Fairy Tale Forest:A brother and sister stumbled upon a fairy tale forest where they met characters from their favorite stories. They went on many adventures with the characters and learned that sometimes the greatest stories are the ones that we write ourselves.",
    "The Magic Island:A young girl discovered a magic island where anything she wished for came true. She used her wishes to help others and learned that sometimes the greatest joy comes from giving to others."
    "The Dragon's Egg:A young boy discovered a dragon's egg and raised the dragon as his own. The dragon grew up to be kind and wise and helped the boy on many adventures. The boy learned that sometimes the greatest friendships can come from the most unexpected places."
    "The Unicorn's Garden:A young girl discovered a secret garden where a unicorn lived. She became friends with the unicorn and helped it tend to the garden. The garden blossomed into a magical wonderland that they shared with others.",
    "The Witch's Curse:A group of adventurers stumbled upon a witch's curse that turned them into animals. They went on a journey to break the curse and learned that sometimes the greatest strength comes from working together."
    "The Mermaid's Pearl:A young boy discovered a mermaid's pearl on the beach. The pearl had the power to grant wishes, but he soon realized that his wishes had unintended consequences. He learned that sometimes the greatest treasures in life are the ones we can't hold in our hands.",
    "The Talking Tree:A young girl discovered a talking tree that had the power to bring people together. The tree taught her about the importance of community and how small acts of kindness can make a big difference",
    "The Enchanted River:A young boy discovered an enchanted river that led him on a magical journey. He met creatures from all over the world and learned that sometimes the greatest adventures are the ones that we least expect.",
    "The Starry Night:A young girl discovered a magic portal in her bedroom that led her to a starry night sky. There, she met a group of friendly aliens who took her on a journey through the galaxy. She learned that sometimes the greatest adventures are the ones that take us far beyond our wildest dreams.",
    "The Enchanted Forest:A group of friends went on a hike through an enchanted forest and stumbled upon a hidden fairy kingdom. The fairies welcomed them and showed them the beauty of nature. The friends learned the importance of respecting the environment and the creatures that inhabit it.",
    "The Dragon's Quest:A young knight went on a quest to defeat a dragon and win the hand of a princess. Along the way, he learned that the dragon was not the monster everyone thought it was, but a gentle creature who just wanted to be understood. He learned that sometimes the greatest battles are the ones that we fight within ourselves.",
    "The Magic Paintbrush:A young artist discovered a magic paintbrush that brought his drawings to life. He used his gift to create a world of beauty and wonder, but soon realized that his gift had a greater purpose. With his art, he helped others see the world in a different way and brought happiness to many.",
    "The Enchanted Book:A young girl found an enchanted book that transported her to a magical world. She went on many adventures with her new friends and learned that sometimes the greatest stories are the ones that we write ourselves.",
    "The Flying Carpet:A young boy discovered a flying carpet that took him on a journey through the clouds. He met many magical creatures along the way and learned that sometimes the greatest adventures are the ones that take us out of our comfort zone.",
    "The Magic Forest:A group of friends stumbled upon a magic forest where the trees came to life. They learned about the importance of protecting nature and the creatures that live within it.",
    "The Crystal Cave:A young girl discovered a crystal cave that was home to a group of fairies. She became friends with the fairies and learned about the power of kindness and the magic of nature.",
    "The Time Traveler:A young boy discovered a time machine that took him on a journey through different eras of history. He met many famous people and learned about the importance of learning from the past and making a positive impact in the present.",
    "The Magic Garden:A young boy discovered a magic garden where the flowers bloomed in different colors every day. He became friends with the garden's caretaker, a wise old wizard, who taught him about the power of imagination and the beauty of diversity. The boy learned that sometimes the greatest magic is found in the world around us."




 



] 
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('A Bedtimestory!'))
    
@client.event
async def on_message(message):
    if message.content.startswith('!bedtimestory'):
        # Send a random bedtime story from the list
        story = random.choice(bedtime_stories)
        await message.channel.send(story)




client.run('MTA4NTIwOTc5MTA2MTgzOTg3Mw.Gcsels.1rQ4kGWUWxRruvUeDjJr_zusfyvcs1mD2BH5bY')
