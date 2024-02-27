using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            StringBuilder sb = new StringBuilder();
            int n = int.Parse(Console.ReadLine());
            for (int i = n / 4; i > 0; i--)
            {
                sb.Append("long ");
            }
            sb.Append("int");

            Console.WriteLine(sb.ToString());
        }
    }
}