from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self, password, user=None):
        # Verification if all caracters in the password are letters or not.
        if not any(char.isaphal() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code="password_no_letter")
    
    # Give a message to the user to help.
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'