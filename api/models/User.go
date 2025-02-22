package models

import (
	"gorm.io/gorm"
)

type User struct {
	UserID   uint    `gorm:"primaryKey;autoIncrement" json:"id"`
	Name     *string `gorm:"type:varchar(255)" json:"name"`
	Email    string  `gorm:"type:varchar(255);unique;not null" json:"email"`
	Password string  `gorm:"type:varchar(255);not null" json:"password"`
}

func MigrateUser(db *gorm.DB) error {
	err := db.AutoMigrate(&User{})
	return err
}
