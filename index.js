const { Client, Events, GatewayIntentBits, Collection } = require('discord.js');

//dotenv
const dotenv = require('dotenv');
dotenv.config()
const {TOKEN } = process.env;

//importacao dos comandos
const fs = require("node:fs")
const path = require("node:path")

const commandsPath = path.join(__dirname, "commands")
const commandFile = fs.readdirSync(commandsPath).filter(file.endsWith(".js"))

const client = new Client({ intents: [GatewayIntentBits.Guilds] });
client.commands = new Collection()

for (const file of commandFiles){
	const filePath = path.join(commandsPath, file)
	const commands = require(filePath)
	if ("data" in command && "execute" in command){
		client.commands.set(command.data.name, comand)
	} else {
		console.log(`Esse comando em ${filePath} está com "data" ou "execute" ausentes`)
	}
}

//Login do bot
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});
client.login(TOKEN);

//Listener de interacoes com o bot
client.on(Events.InteractionCreate, interection =>{
	if (!interection.isChatInputCommand()) return
	console.log(interection)
})