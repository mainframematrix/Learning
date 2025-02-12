using Hierarchical;
using Simple;
using Multiple;
using Abstraction;

namespace Driver
{
    class Driver
    {
        static void Main(string[] args)
        {
            AbstractionDemonstation abstractionDemonstation = new AbstractionDemonstation();
            abstractionDemonstation.demonstate();
            SimpleDemonstation SimpleInheritance = new SimpleDemonstation();
            SimpleInheritance.demonstate();
            HeirarchicalDemonstation heirarchicalInheritance = new HeirarchicalDemonstation();
            heirarchicalInheritance.demonstate();
            MultipleDemonstation multipleInheritance = new MultipleDemonstation();
            multipleInheritance.demonstate();
            
        }
    }
}