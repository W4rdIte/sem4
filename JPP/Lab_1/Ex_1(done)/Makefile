# Compiler
CC := gcc
# Compiler flags
CFLAGS := -Wall -Wextra -g
# Directories
SRCDIR := src
OBJDIR := obj
# Source files
SOURCES := $(wildcard $(SRCDIR)/*.c)
# Object files
OBJECTS := $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(SOURCES))
# Target executable
TARGET := run

# Default target
all: $(TARGET)

# Linking the object files
$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $^ -o $@

# Compiling source files
$(OBJDIR)/%.o: $(SRCDIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up
clean:
	rm -rf $(OBJDIR)/*.o $(TARGET)
