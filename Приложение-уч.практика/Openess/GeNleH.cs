using Smile;

namespace Openess
{
	public static class GeNleH
	{
		public static double[] estimation(int[] usersData)
		{
			string fileName = "code\C#\Openess\Network.xdsl";

			Network net = new Network();
			net.ReadFile(fileName);

			if (usersData[0] > 71) net.SetEvidence("Количество_друзей", "Высокое");
			else net.SetEvidence("Количество_друзей", "Низкое");

			if (usersData[1] > 52) net.SetEvidence("Количество_групп", "Высокое");
			else net.SetEvidence("Количество_групп", "Низкое");


			if (usersData[2] > 1) net.SetEvidence("Частота_постинга", "Высокая");
			else net.SetEvidence("Частота_постинга", "Низкая");

			if (usersData[3] > 4) net.SetEvidence("Частота_лайкания", "Высокая");
			else net.SetEvidence("Частота_лайкания", "Низкая");

			if (usersData[4] > 2) net.SetEvidence("Количество_личной_информации_на_страничке", "Высокое");
			else net.SetEvidence("Количество_личной_информации_на_страничке", "Низкое");

			net.UpdateBeliefs();
			double[] degreeOfOpeness = net.GetNodeValue("Степень_открытости_пользователя_к_принятию_новой_информации");
			return degreeOfOpeness;

		}
	}
}