using System;
using System.Collections.Generic;
using System.Windows.Forms;
using VkNet;
    

namespace Openess
{
    public partial class Form1 : Form
    {
   
        internal static VkApi api;
        internal static Smile.License license;

        public Form1()
        {
           
            InitializeComponent();
        }
        private void textBoxId_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBoxId_KeyPress(object sender, KeyPressEventArgs e)
        {
            char number = e.KeyChar;

            if (!Char.IsDigit(number))
            {
                e.Handled = true;
            }
        }

        private void buttonGo_Click(object sender, EventArgs e)
        {
            labelWait.Text = "Подождите, идет сбор данных";
            labeluHigh.Text = "";
            labeluLow.Text = "";

            int userId = Convert.ToInt32(textBoxId.Text);
            KeyValuePair<string, int[]> usersData = ParserH.getUsersData(Convert.ToInt32(textBoxId.Text), api);
            labeluName.Text = usersData.Key;
            labeluFriend.Text = Convert.ToString(usersData.Value[0]);
            labeluGroup.Text = Convert.ToString(usersData.Value[1]);
            labeluInfo.Text = Convert.ToString(usersData.Value[4]);
            labeluLike.Text = Convert.ToString(usersData.Value[3]);
            labeluPost.Text = Convert.ToString(usersData.Value[2]);
            double[] estimateOfOpeness = GeNleH.estimation(usersData.Value);
            labelHigh.Text = "Высокая:";
            labeluHigh.Text = Convert.ToString(estimateOfOpeness[0]);
            labelLow.Text = "Низкая:";
            labeluLow.Text = Convert.ToString(estimateOfOpeness[1]);

            textBoxId.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void labelInfo_Click(object sender, EventArgs e)
        {

        }

        private void labelName_Click(object sender, EventArgs e)
        {

        }

        private void labelGroup_Click(object sender, EventArgs e)
        {

        }

        private void labelFriends_Click(object sender, EventArgs e)
        {

        }

        private void labelLike_Click(object sender, EventArgs e)
        {

        }

        private void labelPost_Click(object sender, EventArgs e)
        {

        }

        private void labeluName_Click(object sender, EventArgs e)
        {

        }
    }
}

