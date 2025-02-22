package controller

import (
	"errors"
	"os"
	"strings"
	"time"

	"github.com/framewise/models"
	"github.com/gofiber/fiber/v2"
	"github.com/golang-jwt/jwt/v4"
	"github.com/joho/godotenv"
	"golang.org/x/crypto/bcrypt"
	"gorm.io/gorm"
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

func VerifyUser(db *gorm.DB) func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		tokenString := c.Get("Authorization")
		if tokenString == "" {
			return c.Status(401).JSON(fiber.Map{
				"message": "No token found",
			})
		}

		tokenString = tokenString[7:]

		token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
			if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
				return nil, errors.New("invalid token Here")
			}
			return []byte(os.Getenv("SECRET_KEY")), nil
		})

		if err != nil || !token.Valid {
			return c.Status(402).JSON(fiber.Map{
				"message": "Invalid token",
				"error":   err.Error(),
			})
		}

		claims, _ := token.Claims.(jwt.MapClaims)
		UserID := claims["UserID"]
		if UserID == nil {
			return c.Status(403).JSON(fiber.Map{
				"message": "User Id not found in tokens",
				"calims":  claims,
			})
		}

		return c.Status(200).JSON(fiber.Map{
			"message": "User verified",
			"id":      UserID,
		})

	}
}

func CreateUser(db *gorm.DB) func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		user := new(models.User)

		err := c.BodyParser(user)
		if err != nil {
			return c.Status(400).JSON(fiber.Map{
				"message": "Could not parse Body",
				"error":   err.Error(),
			})
		}

		if user.Email == "" || user.Password == "" {
			return c.Status(401).JSON(fiber.Map{
				"message": "Email or Password is missing",
			})
		}

		hasedPassword, err := bcrypt.GenerateFromPassword([]byte(user.Password), bcrypt.DefaultCost)
		if err != nil {
			return c.Status(500).JSON(fiber.Map{
				"message": "Could not hash password",
				"error":   err.Error(),
			})
		}

		user.Password = string(hasedPassword)

		err = db.Create(user).Error
		if err != nil {

			if strings.Contains(err.Error(), "SQLSTATE 23505") {
				return c.Status(402).JSON(fiber.Map{
					"message": "Email already exists",
				})
			}

			return c.Status(501).JSON(fiber.Map{
				"message": "Could not create user",
				"error":   err.Error(),
			})
		}

		token, err := GenerateJWT(user)
		if err != nil {
			return c.Status(502).JSON(fiber.Map{
				"message": "Could not generate token",
				"error":   err.Error(),
			})
		}

		return c.Status(201).JSON(fiber.Map{
			"message": "User created",
			"data":    user,
			"token":   token,
		})
	}
}

func Login(db *gorm.DB) func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		userData := new(models.User)

		err := c.BodyParser(userData)
		if err != nil {
			return c.Status(400).JSON(fiber.Map{
				"message": "Could not parse Body",
				"error":   err.Error(),
			})
		}

		if userData.Email == "" || userData.Password == "" {
			return c.Status(401).JSON(fiber.Map{
				"message": "Email or Password is missing",
			})
		}

		user := new(models.User)
		err = db.Where("email = ?", userData.Email).First(user).Error
		if err != nil {
			if strings.Contains(err.Error(), "record not found") {
				return c.Status(404).JSON(fiber.Map{
					"message": "User not found",
				})
			}

			return c.Status(500).JSON(fiber.Map{
				"message": "Could not retrieve user",
				"error":   err.Error(),
			})
		}

		err = bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(userData.Password))
		if err != nil {
			return c.Status(402).JSON(fiber.Map{
				"message": "Invalid Password",
			})
		}

		token, err := GenerateJWT(user)
		if err != nil {
			return c.Status(502).JSON(fiber.Map{
				"message": "Could not generate token",
				"error":   err.Error(),
			})
		}

		return c.Status(200).JSON(fiber.Map{
			"message": "User logged in",
			"token":   token,
		})
	}
}

func GetUser(db *gorm.DB) func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		id := c.Params("id")

		user := new(models.User)
		err := db.Where("user_id = ?", id).First(user).Error
		if err != nil {
			if strings.Contains(err.Error(), "record not found") {
				return c.Status(404).JSON(fiber.Map{
					"message": "User not found",
				})
			}

			return c.Status(500).JSON(fiber.Map{
				"message": "Could not retrieve user",
				"error":   err.Error(),
			})
		}

		return c.Status(200).JSON(fiber.Map{
			"message": "Retrieved user",
			"data":    user,
		})
	}
}

func GetUsers(db *gorm.DB) func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		users := new([]models.User)

		err := db.Find(users).Error
		if err != nil {
			return c.Status(500).JSON(fiber.Map{
				"message": "Could not retrieve users",
				"error":   err.Error(),
			})
		}

		return c.Status(200).JSON(fiber.Map{
			"message": "Retrieved users",
			"data":    users,
		})
	}
}
