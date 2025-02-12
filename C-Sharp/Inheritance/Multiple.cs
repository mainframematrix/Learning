using System;

namespace Multiple
{
    public interface Engine
    {
        void Vroom();
    }
    public interface Horn
    {
        void Honk();
    }
    class Car : Engine, Horn
    {
        public void Vroom()
        {
            Console.WriteLine($"Engine sounds Vroom.");
        }
        public void Honk()
        {
            Console.WriteLine($"Horn sounds Honk.");
        }
        public void content()
        {
            Console.WriteLine($"I have Engine and Horn.");
        }
    }
    class MultipleDemonstation
    {
        public void demonstate()
        {
            Console.WriteLine("Demonstation of Multiple Inheritance.\n");
            Car c = new Car();
            c.content();
            c.Vroom();
            c.Honk();
            Console.WriteLine("\n\n");
        }
    }
}