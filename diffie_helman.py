# Patrick Canto de Carvalho - 201935026

p = 64151
g = 64483


class User:
    private_key = None

    def get_public_key(self):
        return (g ** self.private_key) % p

    def calculate_secret_key(self, public_key_other):
        return (public_key_other ** self.private_key) % p


alice = User()
alice.private_key = 6405

bob = User()
bob.private_key = 1566

alice_public_key = alice.get_public_key()
bob_public_key = bob.get_public_key()

print(f"Alice calcula chave secreta: {alice.calculate_secret_key(bob_public_key)}")
print(f"Bob calcula chave secreta: {bob.calculate_secret_key(alice_public_key)}")

