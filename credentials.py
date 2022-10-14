class Credentials():
	index = 0
	usernames = []
	passwords = []
	
	def add_cred(self, username, password):
		if username in self.usernames:
			print("User already exists!")
		else:
			self.usernames.append(username)
			self.passwords.append(password)
			self.index+=1
		
	def del_cred(self, index):
		try:
			self.usernames.pop(index)
			self.passwords.pop(index)
			self.index-=1
		except IndexError:
			print("Index does not exist!")
			
	def check_cred(self, username, password):
		if username in self.usernames:
			ind = self.usernames.index(username)
			if password == self.passwords[ind]:
				print("Success")
				return True
			else:
				print("Wrong credentials")
		else:
			print("Wrong credentials")
		return False
		
	def print(self):
		print(f"usernames: {self.usernames}")
		print(f"passwords: {self.passwords}")
		