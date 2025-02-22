package routes

import (
	"github.com/framewise/controller"
	"github.com/gofiber/fiber/v2"
	"gorm.io/gorm"
)

func UserRoutes(db *gorm.DB, app *fiber.App) {
	api := app.Group("/api/v1")
	api.Get("/users/:id", controller.GetUser(db))
	api.Patch("/users/:id", controller.UpdateUser(db))
	api.Post("/register", controller.CreateUser(db))
	api.Post("/login", controller.Login(db))
	api.Get("/verify", controller.VerifyUser(db))
}
