using ClassHierarchicalInheritance;
using Abstraction;

namespace Driver
{
    class Driver
    {
        static void Main(string[] args)
        {
            AbstractionDemonstation abstractionDemonstation = new AbstractionDemonstation();
            abstractionDemonstation.demonstate();
            HeirarchicalDemonstation heirarchicalInheritance = new HeirarchicalDemonstation();
            heirarchicalInheritance.demonstate();
        }
    }
}