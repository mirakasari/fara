//
//  ContentView.swift
//  fara_app
//
//  Created by Mira Kasari on 4/30/26.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    var body: some View {
        TabView {
            NavigationStack { AtlasView() }
                .tabItem { Label("Atlas", systemImage: "globe.asia.australia") }

            NavigationStack { PassportView() }
                .tabItem { Label("Passport", systemImage: "passport") }
        }
    }
}

#Preview {
    ContentView()
        .modelContainer(for: Item.self, inMemory: true)
}
