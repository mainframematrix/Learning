using System;

namespace Simple
{
    abstract class Animal
    {
        public virtual void identity()
        {
            Console.WriteLine($"Hi! I am an Animal.");
        }
    }

    class Dog : Animal
    {
        public override void identity()
        {
            base.identity();
            Console.WriteLine($"I am a Dog.");
        }
    }
    class SimpleDemonstation
    {
        public void demonstate()
        {
            Console.WriteLine("Demonstation of Simple Inheritance.\n");
            Dog dog = new Dog();
            Console.WriteLine("\nDog's Identity:");
            dog.identity();
            Console.WriteLine("\n\n");
        }
    }
}