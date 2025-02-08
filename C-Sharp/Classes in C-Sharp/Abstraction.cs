// Abstration practice
using System;

namespace Abstraction
{

    abstract class Vehicle
    {
        public abstract void StartEngine();

        public void StopEngine()
        {
            Console.WriteLine("Engine stopped.");
        }
    }

    class CarParent : Vehicle
    {
        public override void StartEngine()
        {
            Console.WriteLine("Car engine started.");
        }
        public void EngineSound()
        {
            Console.WriteLine("Vroom");
        }
    }
    class CarChild : CarParent
    {
        public override void StartEngine()

        {
            base.StartEngine();
        }
    }
    class AbstractionDemonstation
    {
        public void demonstate()
        {
            Console.WriteLine("Demonstation of Abstaction in Classes.\n");
            CarParent carParent = new CarParent();
            Console.WriteLine("\nParent Car Class Activities:");
            carParent.StartEngine();  // Output: Car engine started.
            carParent.StopEngine();
            carParent.EngineSound();
            CarChild carChild = new CarChild();
            Console.WriteLine("\nChild Car Class Activities:");
            carChild.StartEngine();
            carChild.EngineSound();
            Console.WriteLine("\n\n");
        }
    }

}