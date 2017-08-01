using System;
using System.Collections.Generic;

namespace collections_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            // Arrays
            int[] zeroTonine = {0,1,2,3,4,6,7,8,9};
            string[] names = {"Tim", "Martin", "Nikki", "Sara"};
            bool[] alternating = {true,false,true,false,true,false,true,false,true,false};


            // Generate Multiplication Table
            int[,] mTable = new int[10,10];
            for(int x = 0; x < 10; x++)
            {
                for(int y = 0; y < 10; y++)
                {
                    mTable[x, y] = (x + 1) * (y + 1);
                }
            }

            // Table Output
            for(int x = 0; x < 10; x++)
            {
                string show = "[ ";
                for(int y = 0; y < 10; y++)
                {
                    if(mTable[x,y] > 99){
                        show += mTable[x, y] + " ";
                    } else {
                        show += mTable[x, y] + ", ";
                    }
                    if(mTable[x,y] < 10)
                    {
                        show += " ";
                    }
                }
                show += "]";
                Console.WriteLine(show);
            }

            // Icecream Flavors
            List<string> flavs = new List<string>();
            flavs.Add("Chocolate");
            flavs.Add("Vanilla");
            flavs.Add("Strawberry");
            flavs.Add("Raspberry");
            flavs.Add("Rocky Road");
            flavs.Add("Turtle");

            // List Length
            Console.WriteLine(flavs.Count);

            // 3rd Value Output and Removed
            Console.WriteLine("The third flavor in the list is: " + flavs[2]);
            flavs.RemoveAt(2);

            // New Length
            Console.WriteLine(flavs.Count);


            // Create Dictionary
            Dictionary<string, string> people = new Dictionary<string,string>();
            Random rand = new Random();
            foreach(string name in names)
            {
                people[name] = flavs[rand.Next(flavs.Count)];
            }

            // Ouput each name with a random flavor
            foreach(KeyValuePair<string, string> info in people)
            {
                Console.WriteLine(info.Key + " - " + info.Value);
            }
        }
    }
}
