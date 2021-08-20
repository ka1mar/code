namespace Openess
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.textBoxId = new System.Windows.Forms.TextBox();
            this.labelName = new System.Windows.Forms.Label();
            this.labelGroup = new System.Windows.Forms.Label();
            this.labelFriends = new System.Windows.Forms.Label();
            this.labelInfo = new System.Windows.Forms.Label();
            this.labelLike = new System.Windows.Forms.Label();
            this.labelPost = new System.Windows.Forms.Label();
            this.labelEstimate = new System.Windows.Forms.Label();
            this.labeluName = new System.Windows.Forms.Label();
            this.labeluGroup = new System.Windows.Forms.Label();
            this.labeluFriend = new System.Windows.Forms.Label();
            this.labeluInfo = new System.Windows.Forms.Label();
            this.labeluLike = new System.Windows.Forms.Label();
            this.labeluPost = new System.Windows.Forms.Label();
            this.labeluHigh = new System.Windows.Forms.Label();
            this.labelWait = new System.Windows.Forms.Label();
            this.labeluLow = new System.Windows.Forms.Label();
            this.labelHigh = new System.Windows.Forms.Label();
            this.labelLow = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(38, 185);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(140, 53);
            this.button1.TabIndex = 0;
            this.button1.Text = "Оценить";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.buttonGo_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.label1.Location = new System.Drawing.Point(38, 105);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(250, 22);
            this.label1.TabIndex = 1;
            this.label1.Text = "Введите Id пользователя:";
            // 
            // textBoxId
            // 
            this.textBoxId.Location = new System.Drawing.Point(38, 148);
            this.textBoxId.Name = "textBoxId";
            this.textBoxId.Size = new System.Drawing.Size(156, 23);
            this.textBoxId.TabIndex = 2;
            this.textBoxId.TextChanged += new System.EventHandler(this.textBoxId_TextChanged);
            this.textBoxId.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBoxId_KeyPress);
            // 
            // labelName
            // 
            this.labelName.AutoSize = true;
            this.labelName.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelName.Location = new System.Drawing.Point(393, 33);
            this.labelName.Name = "labelName";
            this.labelName.Size = new System.Drawing.Size(159, 20);
            this.labelName.TabIndex = 3;
            this.labelName.Text = "Имя и Фамилия:";
            this.labelName.Click += new System.EventHandler(this.labelName_Click);
            // 
            // labelGroup
            // 
            this.labelGroup.AutoSize = true;
            this.labelGroup.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelGroup.Location = new System.Drawing.Point(393, 73);
            this.labelGroup.Name = "labelGroup";
            this.labelGroup.Size = new System.Drawing.Size(129, 20);
            this.labelGroup.TabIndex = 4;
            this.labelGroup.Text = "Число групп:";
            this.labelGroup.Click += new System.EventHandler(this.labelGroup_Click);
            // 
            // labelFriends
            // 
            this.labelFriends.AutoSize = true;
            this.labelFriends.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelFriends.Location = new System.Drawing.Point(393, 113);
            this.labelFriends.Name = "labelFriends";
            this.labelFriends.Size = new System.Drawing.Size(143, 20);
            this.labelFriends.TabIndex = 5;
            this.labelFriends.Text = "Число друзей:";
            this.labelFriends.Click += new System.EventHandler(this.labelFriends_Click);
            // 
            // labelInfo
            // 
            this.labelInfo.AutoSize = true;
            this.labelInfo.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelInfo.Location = new System.Drawing.Point(393, 154);
            this.labelInfo.Name = "labelInfo";
            this.labelInfo.Size = new System.Drawing.Size(253, 40);
            this.labelInfo.TabIndex = 6;
            this.labelInfo.Text = "Кол-во единиц указанной \nличной информации:";
            this.labelInfo.Click += new System.EventHandler(this.labelInfo_Click);
            // 
            // labelLike
            // 
            this.labelLike.AutoSize = true;
            this.labelLike.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelLike.Location = new System.Drawing.Point(393, 220);
            this.labelLike.Name = "labelLike";
            this.labelLike.Size = new System.Drawing.Size(187, 20);
            this.labelLike.TabIndex = 7;
            this.labelLike.Text = "Частота лайкания:";
            this.labelLike.Click += new System.EventHandler(this.labelLike_Click);
            // 
            // labelPost
            // 
            this.labelPost.AutoSize = true;
            this.labelPost.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelPost.Location = new System.Drawing.Point(393, 269);
            this.labelPost.Name = "labelPost";
            this.labelPost.Size = new System.Drawing.Size(185, 20);
            this.labelPost.TabIndex = 8;
            this.labelPost.Text = "Частота постинга:";
            this.labelPost.Click += new System.EventHandler(this.labelPost_Click);
            // 
            // labelEstimate
            // 
            this.labelEstimate.AutoSize = true;
            this.labelEstimate.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelEstimate.Location = new System.Drawing.Point(38, 318);
            this.labelEstimate.Name = "labelEstimate";
            this.labelEstimate.Size = new System.Drawing.Size(364, 22);
            this.labelEstimate.TabIndex = 9;
            this.labelEstimate.Text = "Предполагаемая степень открытости:";
            // 
            // labeluName
            // 
            this.labeluName.AutoSize = true;
            this.labeluName.Location = new System.Drawing.Point(588, 36);
            this.labeluName.Name = "labeluName";
            this.labeluName.Size = new System.Drawing.Size(0, 17);
            this.labeluName.TabIndex = 11;
            this.labeluName.Click += new System.EventHandler(this.labeluName_Click);
            // 
            // labeluGroup
            // 
            this.labeluGroup.AutoSize = true;
            this.labeluGroup.Location = new System.Drawing.Point(588, 76);
            this.labeluGroup.Name = "labeluGroup";
            this.labeluGroup.Size = new System.Drawing.Size(0, 17);
            this.labeluGroup.TabIndex = 12;
            // 
            // labeluFriend
            // 
            this.labeluFriend.AutoSize = true;
            this.labeluFriend.Location = new System.Drawing.Point(588, 115);
            this.labeluFriend.Name = "labeluFriend";
            this.labeluFriend.Size = new System.Drawing.Size(0, 17);
            this.labeluFriend.TabIndex = 13;
            // 
            // labeluInfo
            // 
            this.labeluInfo.AutoSize = true;
            this.labeluInfo.Location = new System.Drawing.Point(662, 177);
            this.labeluInfo.Name = "labeluInfo";
            this.labeluInfo.Size = new System.Drawing.Size(0, 17);
            this.labeluInfo.TabIndex = 14;
            // 
            // labeluLike
            // 
            this.labeluLike.AutoSize = true;
            this.labeluLike.Location = new System.Drawing.Point(588, 218);
            this.labeluLike.Name = "labeluLike";
            this.labeluLike.Size = new System.Drawing.Size(0, 17);
            this.labeluLike.TabIndex = 15;
            // 
            // labeluPost
            // 
            this.labeluPost.AutoSize = true;
            this.labeluPost.Location = new System.Drawing.Point(588, 272);
            this.labeluPost.Name = "labeluPost";
            this.labeluPost.Size = new System.Drawing.Size(0, 17);
            this.labeluPost.TabIndex = 16;
            // 
            // labeluHigh
            // 
            this.labeluHigh.AutoSize = true;
            this.labeluHigh.Location = new System.Drawing.Point(209, 360);
            this.labeluHigh.Name = "labeluHigh";
            this.labeluHigh.Size = new System.Drawing.Size(0, 17);
            this.labeluHigh.TabIndex = 17;
            // 
            // labelWait
            // 
            this.labelWait.AutoSize = true;
            this.labelWait.Location = new System.Drawing.Point(38, 269);
            this.labelWait.Name = "labelWait";
            this.labelWait.Size = new System.Drawing.Size(0, 17);
            this.labelWait.TabIndex = 18;
            // 
            // labeluLow
            // 
            this.labeluLow.AutoSize = true;
            this.labeluLow.Location = new System.Drawing.Point(209, 396);
            this.labeluLow.Name = "labeluLow";
            this.labeluLow.Size = new System.Drawing.Size(0, 17);
            this.labeluLow.TabIndex = 19;
            // 
            // labelHigh
            // 
            this.labelHigh.AutoSize = true;
            this.labelHigh.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point);
            this.labelHigh.Location = new System.Drawing.Point(74, 360);
            this.labelHigh.Name = "labelHigh";
            this.labelHigh.Size = new System.Drawing.Size(0, 18);
            this.labelHigh.TabIndex = 20;
            // 
            // labelLow
            // 
            this.labelLow.AutoSize = true;
            this.labelLow.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point);
            this.labelLow.Location = new System.Drawing.Point(74, 396);
            this.labelLow.Name = "labelLow";
            this.labelLow.Size = new System.Drawing.Size(0, 18);
            this.labelLow.TabIndex = 21;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 17F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.GhostWhite;
            this.ClientSize = new System.Drawing.Size(800, 478);
            this.Controls.Add(this.labelLow);
            this.Controls.Add(this.labelHigh);
            this.Controls.Add(this.labeluLow);
            this.Controls.Add(this.labelWait);
            this.Controls.Add(this.labeluHigh);
            this.Controls.Add(this.labeluPost);
            this.Controls.Add(this.labeluLike);
            this.Controls.Add(this.labeluInfo);
            this.Controls.Add(this.labeluFriend);
            this.Controls.Add(this.labeluGroup);
            this.Controls.Add(this.labeluName);
            this.Controls.Add(this.labelEstimate);
            this.Controls.Add(this.labelPost);
            this.Controls.Add(this.labelLike);
            this.Controls.Add(this.labelInfo);
            this.Controls.Add(this.labelFriends);
            this.Controls.Add(this.labelGroup);
            this.Controls.Add(this.labelName);
            this.Controls.Add(this.textBoxId);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.Name = "Form1";
            this.Text = "Оценка степени открытости к восприятию информации";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        public System.Windows.Forms.TextBox textBoxId;
        private System.Windows.Forms.Label labelName;
        private System.Windows.Forms.Label labelGroup;
        private System.Windows.Forms.Label labelFriends;
        private System.Windows.Forms.Label labelInfo;
        private System.Windows.Forms.Label labelLike;
        private System.Windows.Forms.Label labelPost;
        private System.Windows.Forms.Label labelEstimate;
        private System.Windows.Forms.Label labeluName;
        private System.Windows.Forms.Label labeluGroup;
        private System.Windows.Forms.Label labeluFriend;
        private System.Windows.Forms.Label labeluInfo;
        private System.Windows.Forms.Label labeluLike;
        private System.Windows.Forms.Label labeluPost;
        private System.Windows.Forms.Label labeluHigh;
        private System.Windows.Forms.Label labelWait;
        private System.Windows.Forms.Label labeluLow;
        private System.Windows.Forms.Label labelHigh;
        private System.Windows.Forms.Label labelLow;
    }
}

