Quickstart
=======================================

Download the package from NuGet and add it to your project.json file.

.. highlight:: xml

::

	<Project Sdk="Microsoft.NET.Sdk.Web">
	  <PropertyGroup>
		<TargetFramework>netcoreapp2.0</TargetFramework>
	  </PropertyGroup>
	  <ItemGroup>
		<PackageReference Include="Microsoft.AspNetCore.All" Version="2.0.0" />
		<PackageReference Include="Microsoft.EntityFrameworkCore.Sqlite" Version="2.0.0" />
		<PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="2.0.0" />
		<PackageReference Include="Localization.SqlLocalizer" Version="2.0.1" />
	  </ItemGroup>
	  <ItemGroup>
		<DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="2.0.0" />
		<DotNetCliToolReference Include="Microsoft.Extensions.SecretManager.Tools" Version="2.0.0" />
		<DotNetCliToolReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Tools" Version="2.0.0" />
	  </ItemGroup>
	  <ItemGroup>
		<Folder Include="Migrations\" />
	  </ItemGroup>
	  <PropertyGroup Condition=" '$(Configuration)' == 'Release' ">
		<DefineConstants>$(DefineConstants);RELEASE</DefineConstants>
	  </PropertyGroup>
	</Project>


See EF Core for more details on installing updating a provider


.. highlight:: csharp

Add the configuration to the Startup::

	public void ConfigureServices(IServiceCollection services)
	{
		// init database for localization
		var sqlConnectionString = Configuration["DbStringLocalizer:ConnectionString"];

		services.AddDbContext<LocalizationModelContext>(options =>
			options.UseSqlite(
				sqlConnectionString,
				b => b.MigrationsAssembly("Angular2LocalizationAspNetCore")
			),
			ServiceLifetime.Singleton,
			ServiceLifetime.Singleton
		);

		var useTypeFullNames = true;
		var useOnlyPropertyNames = false;
		var returnOnlyKeyIfNotFound = false;

		// Requires that LocalizationModelContext is defined
		services.AddSqlLocalization(options => options.UseSettings(useTypeFullNames, useOnlyPropertyNames, returnOnlyKeyIfNotFound));
		// services.AddSqlLocalization(options => options.ReturnOnlyKeyIfNotFound = true);
		// services.AddLocalization(options => options.ResourcesPath = "Resources");

		services.AddMvc()
			.AddViewLocalization()
			.AddDataAnnotationsLocalization();

		services.AddScoped<LanguageActionFilter>();

		services.Configure<RequestLocalizationOptions>(
			options =>
				{
					var supportedCultures = new List<CultureInfo>
					{
						new CultureInfo("en-US"),
						new CultureInfo("de-CH"),
						new CultureInfo("fr-CH"),
						new CultureInfo("it-CH")
					};

					options.DefaultRequestCulture = new RequestCulture(culture: "en-US", uiCulture: "en-US");
					options.SupportedCultures = supportedCultures;
					options.SupportedUICultures = supportedCultures;
				});
	}


.. highlight:: csharp

And also the Configure method in the Startup.cs::

	public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
	{
		loggerFactory.AddConsole();
		loggerFactory.AddDebug();

		var locOptions = app.ApplicationServices.GetService<IOptions<RequestLocalizationOptions>>();
		app.UseRequestLocalization(locOptions.Value);

		app.UseStaticFiles();

		app.UseMvc();
	}
	

.. highlight:: csharp

Use migrations to create the database if required::

	dotnet ef migrations add Localization --context LocalizationModelContext
 
	dotnet ef database update Localization --context LocalizationModelContext

	
.. highlight:: csharp

Use like the standard localization::

	using Microsoft.AspNetCore.Mvc;
	using Microsoft.Extensions.Localization;
	 
	namespace AspNet5Localization.Controllers
	{
		[Route("api/[controller]")]
		public class AboutController : Controller
		{
			private readonly IStringLocalizer<SharedResource> _localizer;
			private readonly IStringLocalizer<AboutController> _aboutLocalizerizer;
	 
			public AboutController(IStringLocalizer<SharedResource> localizer, IStringLocalizer<AboutController> aboutLocalizerizer)
			{
				_localizer = localizer;
				_aboutLocalizerizer = aboutLocalizerizer;
			}
	 
			[HttpGet]
			public string Get()
			{
				// _localizer["Name"] 
				return _aboutLocalizerizer["AboutTitle"];
			}
		}
	}