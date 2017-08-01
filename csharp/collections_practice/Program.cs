using System;

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
        }
    }
}
