//
//  WebDriverAgentRunnerApp.swift
//  WebDriverAgentRunner
//
//  Created by Jacqueline Escalante on 20/1/25.
//

import SwiftUI

@main
struct WebDriverAgentRunnerApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
