using System;

namespace first_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            // for (int i = 1; i <= 255; i++)
            // {
            //     Console.WriteLine(i);
            // }

            // for (int i = 1; i <= 100; i++)
            // {
            //     if(i%5 == 0 || i%3 == 0) {
            //      Console.WriteLine(i);
            //     }
            // }

            String msg = "";

            for (int i = 1; i <= 100; i++) {
                if(i%3 == 0) {
                    msg = "Fizz";
                    if(i%5 == 0){
                        msg += " Buzz";
                    }
                } else if (i%5 == 0){
                    msg = "Buzz";
                }

                if(msg != ""){
                    Console.WriteLine(msg);
                }
                msg = "";
            }
        }
    }
}
