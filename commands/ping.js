const { SlashComandBuilder } = require("discord.js")

module.exports = {
    data: new SlashComandBuilder()
        .setName("ping")
        .setDescription("Responde com 'Pong!'"),

    async execute(interaction){
        await interaction.reply("Pong!")
    }
}