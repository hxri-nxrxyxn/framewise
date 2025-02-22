package database

import (
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func NewConnection() (*gorm.DB, error) {

	err := godotenv.Load(".env")
	if err != nil {
		log.Fatal(err)
	}

	dsn := fmt.Sprintf(
		"host=%s port=%s password=%s user=%s dbname=%s sslmode=%s",
		os.Getenv("DB_HOST"), os.Getenv("DB_PORT"), os.Getenv("DB_PASSWORD"), os.Getenv("DB_USER"), os.Getenv("DB_NAME"), os.Getenv("DB_SSLMODE"))
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		return db, err
	}
	return db, nil
}