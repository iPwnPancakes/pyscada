import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { routes as deviceRoutes } from './pages/devices/routes';
import { HttpClientModule } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
    providers: [
        provideRouter(routes),
        provideAnimationsAsync(),
        provideRouter(deviceRoutes),
        importProvidersFrom(HttpClientModule)
    ]
};
