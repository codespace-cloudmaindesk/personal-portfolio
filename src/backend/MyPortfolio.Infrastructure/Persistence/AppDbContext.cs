using Microsoft.EntityFrameworkCore;

namespace MyPortfolio.Infrastructure.Persistence
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        // DbSets will go here, e.g.:
        // public DbSet<Project> Projects { get; set; }
    }
}
