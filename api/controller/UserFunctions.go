package controller

import (
	"errors"
	"os"
	"time"

	"github.com/framewise/models"
	"github.com/golang-jwt/jwt/v4"
	"github.com/joho/godotenv"
)

func GenerateJWT(user *models.User) (string, error) {
	err := godotenv.Load(".env")
	if err != nil {
		return "", err
	}

	key := (os.Getenv("SECRET_KEY"))
	if key == "" {
		return "", errors.New("SECRET_KEY not found")
	}

	claims := jwt.MapClaims{
		"UserID": user.UserID,
		"Email":  user.Email,
		"exp":    time.Now().Add(time.Hour * 24).Unix(),
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenString, err := token.SignedString([]byte(key))
	if err != nil {
		return "", err
	}
	return tokenString, nil
}
