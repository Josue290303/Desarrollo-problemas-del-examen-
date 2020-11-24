namespace RecursividadEjer
{
    class Program
    {
        static void Main(string[] args)
        {
            static void RecursiveMehtod(int variable, int iterationNumber)
            {
                if (Math.Pow(variable, iterationNumber) > 1)
                {
                    Console.WriteLine((variable) * (Math.Pow(variable, iterationNumber - 1)));
                    RecursiveMehtod(variable - 1, iterationNumber - 1);
                }
            }

            RecursiveMehtod(10, 9);
        }
    }
}
